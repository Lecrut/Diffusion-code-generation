def hex_strings_to_integers(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    result = hex_strings_to_integers(['00', '10', 'ff', 'a1b2'])
    print(result)