def pascal_to_psi(pascals):
    return pascals / 6894.75729

def psi_to_pascal(psi):
    return psi * 6894.75729

def pascal_to_atm(pascals):
    return pascals / 101325

def atm_to_pascal(atm):
    return atm * 101325

def psi_to_atm(psi):
    return psi / 14.695948

def atm_to_psi(atm):
    return atm * 14.695948
if __name__ == '__main__':
    print(pascal_to_psi(101325))
    print(psi_to_pascal(15))
    print(pascal_to_atm(101325))
    print(atm_to_pascal(1.0))
    print(psi_to_atm(14.695948))
    print(atm_to_psi(1.0))