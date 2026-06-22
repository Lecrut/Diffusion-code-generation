def km_to_m_generator():
    km_values = [1, 2.5, 3, 10, 0.1]
    for km in km_values:
        yield km * 1000

if __name__ == '__main__':
    generator = km_to_m_generator()
    for value in generator:
        print(value)