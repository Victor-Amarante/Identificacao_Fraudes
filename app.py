import streamlit as st
from PIL import Image

def comparar_assinaturas(img1, img2):
    # Pré-processa as imagens para melhorar a qualidade e eliminar o ruído
    img1 = img1.convert('L')
    img2 = img2.convert('L')
    
    # Extrai as características das duas imagens usando a técnica de diferença de histograma
    hist1 = img1.histogram()
    hist2 = img2.histogram()
    diff = sum((h1 - h2)**2 for h1, h2 in zip(hist1, hist2))**0.5
    
    # Calcula a porcentagem de similaridade entre as duas imagens
    similaridade = (1 - (diff / (img1.size[0]*img1.size[1]*len(img1.getbands())))) * 100
    
    # Verifica se as duas assinaturas são consideradas iguais ou diferentes com base no limite de similaridade definido
    if similaridade > 98:
        return True, similaridade
    else:
        return False, similaridade

st.set_page_config(page_title='Tratamento Automático',
                    layout='wide')

with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2019/12/shutterstock_1166533285-Converted-02.png')
    st.title('Identificação de Fraudes')
    st.info('Esse projeto irá auxiliar na identificação de fraudes por meio da comparação de assinaturas.')

st.title('Comparador de assinaturas')

# Carregar as duas assinaturas nos formatos adequados
img1 = st.file_uploader('Carregar imagem 1', type=['jpg', 'jpeg', 'png'])
img2 = st.file_uploader('Carregar imagem 2', type=['jpg', 'jpeg', 'png'])

st.markdown('---')

if img1 and img2:
    # Converte as imagens para o formato PIL
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(img1, use_column_width=True)
    with col2:
        st.image(img2, use_column_width=True)
    # Compara as duas imagens de assinatura
    igual, similaridade = comparar_assinaturas(img1, img2)
    
    # Mostra ao usuário se as duas assinaturas são consideradas iguais ou diferentes e a porcentagem de similaridade entre elas
    if igual:
        st.success(f'As duas assinaturas são consideradas iguais com {similaridade:.2f}% de similaridade.')
    else:
        st.warning(f'As duas assinaturas são consideradas diferentes com {similaridade:.2f}% de similaridade.')
