def m_to_f(miles):
    assert isinstance(miles, (int, float))
    return miles * 5280
if __name__ == '__main__':
    print(m_to_f(1))
    print(m_to_f(2.5))