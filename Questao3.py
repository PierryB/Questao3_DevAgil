def digital_root(n):
    """
    Calcula a raiz digital de um número não negativo.
    
    Parâmetros:
    n (int): Número inteiro não negativo.
    
    Retorna:
    int: O dígito único resultante após a aplicação do processo de soma recursiva.
    """
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))

# Testes Unitários
def teste_digital_root():
    # Teste para número de 1 dígito
    assert digital_root(4) == 4

    # Teste para número de 2 dígitos
    assert digital_root(16) == 7

    # Teste para número de 3 dígitos
    assert digital_root(345) == 3

    # Teste para número de 4 dígitos
    assert digital_root(2014) == 7

    # Teste para número de 6 dígitos
    assert digital_root(123451) == 7

    # Teste para número de 6 dígitos diferentes
    assert digital_root(789654) == 3

# Executando os testes unitários se este arquivo for executado diretamente
if __name__ == '__main__':
    teste_digital_root()
    print("Testes passaram com sucesso!")