def m_to_f(miles):
    return miles * 5280

if __name__ == '__main__':
    sample_miles = 3.25
    converted_feet = m_to_f(sample_miles)
    print(converted_feet)
    another_miles = 10
    print(m_to_f(another_miles))