import streamlit as st

# Configuração da página
st.set_page_config(page_title="Simulador Supernorte", layout="centered")

# Título e cabeçalho
st.title("🛒 Simulador de Pontos e Desconto")
#st.write("Regra: **R$ 1 comprado = 1 Ponto**. A cada **125 pontos**, ganha-se **R$ 1,00 de desconto**.")
st.divider()

# Entradas de dados
col_input1, col_input2 = st.columns(2)

with col_input1:
    preco_unitario = st.number_input(
        "Preço do Produto/Caixa (R$):", 
        min_value=0.0, 
        step=5.0, 
        format="%.2f"
    )

with col_input2:
    quantidade = st.number_input(
        "Quantidade (Caixas):", 
        min_value=1, 
        step=1
    )

# Lógica de cálculo matemático
valor_total_compra = preco_unitario * quantidade

if valor_total_compra > 0:
    # Cálculos Totais
    pontos_ganhos = valor_total_compra
    valor_desconto_total = pontos_ganhos / 125
    valor_final_total = valor_total_compra - valor_desconto_total
    
    # Cálculos Unitários (Por Caixa)
    desconto_por_caixa = valor_desconto_total / quantidade
    preco_final_por_caixa = preco_unitario - desconto_por_caixa

    # Exibição do Subtotal
    st.markdown(f"### Subtotal sem desconto: R$ {valor_total_compra:,.2f}".replace(".", ","))
    st.write("")
    
    # Bloco 1: Detalhamento por Caixa
    st.subheader("📦 Detalhamento por Caixa")
    col1_caixa, col2_caixa = st.columns(2)
    col1_caixa.metric("Desconto por Caixa", f"R$ {desconto_por_caixa:,.2f}".replace(".", ","))
    col2_caixa.metric("Preço Final da Caixa", f"R$ {preco_final_por_caixa:,.2f}".replace(".", ","))
    
    st.divider()
    
    # Bloco 2: Totais da Fatura
    st.subheader("🛒 Resultado Total da Fatura")
    col1_tot, col2_tot, col3_tot = st.columns(3)
    col1_tot.metric("Pontos Adquiridos", f"{pontos_ganhos:,.0f}".replace(",", "."))
    col2_tot.metric("Desconto Total", f"R$ {valor_desconto_total:,.2f}".replace(".", ","))
    col3_tot.metric("Fatura Final", f"R$ {valor_final_total:,.2f}".replace(".", ","))