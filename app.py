import streamlit as st

st.set_page_config(page_title="Campo de Futebol 3D", layout="centered")

# HTML e CSS do campo
campo_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <style>
    body {
      margin: 0;
      background: #2e7d32;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      perspective: 1000px;
    }
    .campo {
      position: relative;
      width: 800px;
      height: 500px;
      background: #388e3c;
      border: 10px solid white;
      box-shadow: 0 0 0 10px white inset;
      transform-style: preserve-3d;
    }
    .linha-central, .meio-campo, .grande-area, .pequena-area, .ponto-penalti, .meia-lua {
      position: absolute;
      border: 4px solid white;
      box-sizing: border-box;
    }
    .linha-central {
      top: 0;
      left: 50%;
      width: 0;
      height: 100%;
      border-left: 4px solid white;
    }
    .meio-campo {
      width: 120px;
      height: 120px;
      top: 50%;
      left: 50%;
      border-radius: 50%;
      transform: translate(-50%, -50%);
    }
    .grande-area {
      width: 120px;
      height: 320px;
      top: 90px;
      left: 0;
    }
    .grande-area.direita {
      left: auto;
      right: 0;
    }
    .pequena-area {
      width: 60px;
      height: 160px;
      top: 170px;
      left: 0;
    }
    .pequena-area.direita {
      left: auto;
      right: 0;
    }
    .ponto-penalti {
      width: 8px;
      height: 8px;
      background: white;
      border: none;
      border-radius: 50%;
      top: 246px;
      left: 100px;
    }
    .ponto-penalti.direita {
      left: auto;
      right: 100px;
    }
    .meia-lua {
      width: 80px;
      height: 160px;
      top: 170px;
      left: 120px;
      border-radius: 50%;
      border-left: none;
      border-right: 4px solid white;
    }
    .meia-lua.direita {
      left: auto;
      right: 120px;
      border-left: 4px solid white;
      border-right: none;
    }
    .trave {
      position: absolute;
      width: 60px;
      height: 160px;
      top: 170px;
      background: transparent;
      transform: translateZ(40px) rotateY(10deg);
      border: 6px solid white;
      box-sizing: border-box;
      box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
    }
    .trave.direita {
      right: -33px;
      transform: translateZ(40px) rotateY(-10deg);
    }
    .trave.esquerda {
      left: -33px;
    }
  </style>
</head>
<body>
  <div class="campo">
    <div class="linha-central"></div>
    <div class="meio-campo"></div>
    <div class="grande-area"></div>
    <div class="grande-area direita"></div>
    <div class="pequena-area"></div>
    <div class="pequena-area direita"></div>
    <div class="ponto-penalti"></div>
    <div class="ponto-penalti direita"></div>
    <div class="meia-lua"></div>
    <div class="meia-lua direita"></div>
    <div class="trave esquerda"></div>
    <div class="trave direita"></div>
  </div>
</body>
</html>
"""

# Título e exibição
st.title("🏟️ Campo de Futebol com Traves em 3D")
st.components.v1.html(campo_html, height=600)
