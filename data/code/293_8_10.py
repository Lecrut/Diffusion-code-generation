def pascal_to_psi(pascals):
    return pascals * 0.000145038

def pascal_to_atm(pascals):
    return pascals * 9.86923e-06

def psi_to_pascal(psi):
    return psi / 0.000145038

def psi_to_atm(psi):
    return psi * 0.068046

def atm_to_pascal(atm):
    return atm / 9.86923e-06

def atm_to_psi(atm):
    return atm / 0.068046
if __name__ == '__main__':
    print(pascal_to_psi(100000))
    print(pascal_to_atm(100000))
    print(psi_to_pascal(70))
    print(psi_to_atm(70))
    print(atm_to_pascal(1))
    print(atm_to_psi(1))