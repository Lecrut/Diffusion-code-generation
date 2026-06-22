def kilometers_to_meters(kilometers):
    CONVERSION_FACTOR = 1000
    meters = kilometers * CONVERSION_FACTOR
    return meters
if __name__ == '__main__':
    km_value = 5.0
    m_value = kilometers_to_meters(km_value)
    print(m_value)