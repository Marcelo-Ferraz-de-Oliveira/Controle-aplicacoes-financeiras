from webapp.extrator import str_to_br_currency, extrair_dados
import pytest
from os.path import dirname, join

PDF_DIR = join(dirname(dirname(dirname(__file__))),"notas_pdf")

def test_str_to_br_currency():
      assert str_to_br_currency('1.432,00') == "1432.00"
      assert str_to_br_currency('600,00') == "600.00"
      assert str_to_br_currency('500,32') == "500.32"
      assert str_to_br_currency('1.432,32') == "1432.32"
      with pytest.raises(ValueError):
            str_to_br_currency(1432)
            str_to_br_currency(["100","200"])
            
def test_extrair_dados():
      #Open file with multiple pages and password protected
      result_multiple = [{'nota': 842471, 'folha': 1, 'data': '24/01/2022', 'corretora': 'Clear', 'negocios': [{'index': 0, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'V', 'tipo_mercado': 'OPCAO DE COMPRA', 'prazo': '02/22', 'nome_pregao': 'ABEVB161ON 15.62ABEVE', 'obs': '', 'quantidade': 3900.0, 'preco': 0.21, 'valor_operacao': 819.0, 'dc': 'C', 'codigo': 'ABEVB161', 'custo_proporcional': 0.4095}, {'index': 1, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'V', 'tipo_mercado': 'OPCAO DE COMPRA', 'prazo': '02/22', 'nome_pregao': 'ABEVB161ON 15.62ABEVE', 'obs': '', 'quantidade': 3900.0, 'preco': 0.21, 'valor_operacao': 819.0, 'dc': 'C', 'codigo': 'ABEVB161', 'custo_proporcional': 0.4095}, {'index': 2, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'V', 'tipo_mercado': 'OPCAO DE COMPRA', 'prazo': '02/22', 'nome_pregao': 'ABEVB161ON 15.62ABEVE', 'obs': '', 'quantidade': 1600.0, 'preco': 0.21, 'valor_operacao': 336.0, 'dc': 'C', 'codigo': 'ABEVB161', 'custo_proporcional': 0.168}, {'index': 3, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'V', 'tipo_mercado': 'OPCAO DE COMPRA', 'prazo': '02/22', 'nome_pregao': 'ABEVB161ON 15.62ABEVE', 'obs': '', 'quantidade': 100.0, 'preco': 0.26, 'valor_operacao': 26.0, 'dc': 'C', 'codigo': 'ABEVB161', 'custo_proporcional': 0.013}], 'custos': {'Taxa de liquidação': 0.55, 'Taxa de Registro': 1.39, 'Taxa de termo/opções': 0.0, 'Taxa A.N.A.': 0.0, 'Emolumentos': 0.74, 'Taxa Operacional': 0.0, 'Execução': 0.0, 'Taxa de Custódia': 0.0, 'Impostos': 0.0, 'I.R.R.F. s/ operações, base R$2.000,00': 0.1, 'Outros': 0.0, 'total': 2.78}}, {'nota': 842470, 'folha': 2, 'data': '24/01/2022', 'corretora': 'Clear', 'negocios': [{'index': 0, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.98, 'valor_operacao': 1498.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010827611131189014}, {'index': 1, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 600.0, 'preco': 14.98, 'valor_operacao': 8988.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.06496566678713409}, {'index': 2, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.82, 'valor_operacao': 1482.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010711962414166968}, {'index': 3, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 200.0, 'preco': 14.83, 'valor_operacao': 2966.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.021438380917961693}, {'index': 4, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 600.0, 'preco': 14.83, 'valor_operacao': 8898.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.06431514275388507}, {'index': 5, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.84, 'valor_operacao': 1484.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010726418503794723}, {'index': 6, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 300.0, 'preco': 14.83, 'valor_operacao': 4449.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.032157571376942536}, {'index': 7, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 500.0, 'preco': 14.98, 'valor_operacao': 7490.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.054138055655945067}, {'index': 8, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 400.0, 'preco': 14.98, 'valor_operacao': 5992.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.043310444524756055}, {'index': 9, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 1800.0, 'preco': 14.83, 'valor_operacao': 26694.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.19294542826165523}, {'index': 10, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON #', 'obs': '', 'quantidade': 100.0, 'preco': 14.82, 'valor_operacao': 1482.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010711962414166968}, {'index': 11, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.83, 'valor_operacao': 1483.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010719190458980846}, {'index': 12, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON #', 'obs': '', 'quantidade': 700.0, 'preco': 14.98, 'valor_operacao': 10486.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.07579327791832309}, {'index': 13, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.81, 'valor_operacao': 1481.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.01070473436935309}, {'index': 14, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 400.0, 'preco': 14.98, 'valor_operacao': 5992.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.043310444524756055}, {'index': 15, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 2900.0, 'preco': 14.84, 'valor_operacao': 43036.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.311066136610047}, {'index': 16, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 200.0, 'preco': 14.83, 'valor_operacao': 2966.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.021438380917961693}, {'index': 17, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.83, 'valor_operacao': 1483.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.010719190458980846}, {'index': 18, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.82, 'valor_operacao': 1482.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.49731543624161073}, {'index': 19, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/AON', 'obs': '', 'quantidade': 100.0, 'preco': 14.98, 'valor_operacao': 1498.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 0.5026845637583892}], 'custos': {'Taxa de liquidação': 35.33, 'Taxa de Registro': 0.0, 'Taxa de termo/opções': 0.0, 'Taxa A.N.A.': 0.0, 'Emolumentos': 7.06, 'Taxa Operacional': 0.0, 'Execução': 0.0, 'Taxa de Custódia': 0.0, 'Impostos': 0.0, 'I.R.R.F. s/ operações, base R$0,00': 0.0, 'Outros': 0.0, 'total': 42.39}}]
      test_multiple = extrair_dados(join(PDF_DIR,"nota-de-corretagem-clear-multiplas-paginas.pdf"), "007")
      assert result_multiple == test_multiple
      result_genial = [{'nota': 1037, 'folha': 1, 'data': '30/06/2020', 'corretora': 'Genial', 'negocios': [{'index': 0, 'q': '', 'negociacao': '1-BOVESPA', 'cv': 'C', 'tipo_mercado': 'VISTA', 'prazo': '', 'nome_pregao': 'AMBEV S/A ON', 'obs': '', 'quantidade': 300.0, 'preco': 14.27, 'valor_operacao': 4281.0, 'dc': 'D', 'codigo': 'ABEV3', 'custo_proporcional': 1.0}], 'custos': {'Taxa de liquidação': 1.17, 'Taxa de Registro': 0.0, 'Taxa de termo/opções': 0.0, 'Taxa A.N.A.': 0.0, 'Emolumentos': 0.14, 'Clearing': 5.0, 'Execução': 0.0, 'Execução casa': 0.0, 'ISS ( SÃO PAULO )': 0.25, 'ISS/PIS/COFINS': 0.48, 'total': 7.04}}]
      test_genial = extrair_dados(join(PDF_DIR,"nota-de-corretagem-genial.pdf"),"")
      assert result_genial == test_genial
      with pytest.raises(FileNotFoundError):
            extrair_dados("wrong_filename","")
      with pytest.raises(FileNotFoundError):
            extrair_dados(join(PDF_DIR,"null.pdf"),"")
      with pytest.raises(ValueError):
            extrair_dados(join(PDF_DIR,"nota_invalida.pdf"),"")
            #TODO teste de corretora não suportada

      
      