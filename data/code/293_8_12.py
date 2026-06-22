def pascal_to_psi(pascals):
    return pascals * 0.000145038

def psi_to_pascal(psi):
    return psi / 0.000145038

def pascal_to_atm(pascals):
    return pascals * 9.86923e-6

def atm_to_pascal(atm):
    return atm / 9.86923e-6

def psi_to_atm(psi):
    return psi * 0.0680459

def atm_to_psi(atm):
    return atm / 0.0680459

if __name__ == '__main__':
    print(f"1000 pascals is {pascal_to_psi(1000):.2f} psi")
    print(f"15 psi is {psi_to_pascal(15):.2f} pascals")
    print(f"1000 pascals is {pascal_to_atm(1000):.6f} atm")
    print(f"1 atm is {atm_to_pascal(1):.2f} pascals")
    print(f"15 psi is {psi_to_atm(15):.6f} atm")
    print(f"1 atm is {atm_to_psi(1):.2f} psi")