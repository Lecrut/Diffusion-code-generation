Kilometers_to_meters = 1000

def kilometers_to_meters(kilometers):
    return kilometers * Kilometers_to_meters

if __name__ == '__main__':
    km_value = 5
    m_value = kilometers_to_meters(km_value)
    print(m_value)