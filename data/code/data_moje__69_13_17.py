def m_to_f(miles):
    if not isinstance(miles, (int, float)):
        raise TypeError("Input must be a numeric value")
    return miles * 5280

if __name__ == '__main__':
    print(m_to_f(1))
    print(m_to_f(1.5))
    print(m_to_f(0))
    print(m_to_f(5280))