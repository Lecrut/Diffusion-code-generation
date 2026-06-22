CONVERSION_FACTOR = 5280
def m_to_f(miles): return miles * CONVERSION_FACTOR
if __name__ == '__main__':
    print(m_to_f(1))
    print(m_to_f(2.5))