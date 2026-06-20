if __name__ == '__main__':
    boolean_values = {True: False, False: True}
    for value in boolean_values:
        inverted_value = not value
        print(f"Original {value}: {inverted_value}")