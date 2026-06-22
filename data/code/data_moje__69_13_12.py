CONVERSION_FACTOR = 5280

def m_to_f(miles):
    if miles == 0:
        return 0
    return miles * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 10.5
    result = m_to_f(sample_miles)
    print(result)
    print(m_to_f(0))