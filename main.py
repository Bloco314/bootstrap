from flask import Flask, render_template

app = Flask(__name__)

def retorna_opcoes_de_meses_bd():
    return ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
def retorna_dados_setor_bd():
    return [
        ['setor1',10,0,0,0,0,0],
        ['setor2',20,0,0,0,0,0],
        ['setor3',30,0,0,0,0,0],
        ['setor4',40,0,0,0,0,0],
        ['setor5',60,0,0,0,0,0],
        ['setor6',70,0,0,0,0,0],
        ['setor7',80,0,0,0,0,0],
        ['setor8',80,0,0,0,0,0],
        ['setor9',80,0,0,0,0,0]
    ]

@app.route('/')
def index():
    return render_template('infra_usuario.html')

@app.route('/infra')
def infra():
    meses = retorna_opcoes_de_meses_bd()
    setores = retorna_dados_setor_bd()
    num_textos = len(setores)
    num_linhas = (num_textos - 1) // 3 + 1  # 3 é o número de colunas que queremos
    num_colunas = (num_textos - 1) // num_linhas + 1
   
    return render_template('infra_setor.html', meses=meses, textos=setores, num_linhas=num_linhas, num_colunas=num_colunas, num_textos=num_textos)
  

if __name__ == '__main__':
    app.run(debug=True)
