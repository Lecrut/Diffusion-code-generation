conversion_factors = {'feet': 304800}

def feet_to_micrometers(feet):
    return feet * conversion_factors['feet']

if __name__ == '__main__':
    print(feet_to_micrometers(1))
    print(feet_to_micrometers(5))
    print(feet_to_micrometers(10))