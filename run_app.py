import os
import sys
import webbrowser
from threading import Timer
from app import app

def open_browser():
    # Abre o navegador automaticamente
    webbrowser.open_new("http://127.0.0.1:5000/")

def main():
    # Timer para abrir o navegador após o servidor subir
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1.5, open_browser).start()
    try:
        # Roda o app na porta 5000
        app.run(port=5000, debug=False)
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}", file = sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()