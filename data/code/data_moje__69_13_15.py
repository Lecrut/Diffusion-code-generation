CONVERSION_FACTOR = 5280

def m_to_f(miles):
    return miles * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = [0, 1, 1.5, 100]
    for value in sample_miles:
        print(m_to_f(value))