MASK = 1

def get_bitwise_opposite(flag):
    inverted = ~flag
    result = inverted & MASK
    return bool(result)

if __name__ == '__main__':
    initial_true = True
    initial_false = False
    output_true = get_bitwise_opposite(initial_true)
    output_false = get_bitwise_opposite(initial_false)
    print(output_true)
    print(output_false)