BIT_MASK = 1

def get_bitwise_negation(boolean_input):
    inverted_value = ~boolean_input
    masked_result = inverted_value & BIT_MASK
    return bool(masked_result)

if __name__ == '__main__':
    val_true = True
    val_false = False
    print(get_bitwise_negation(val_true))
    print(get_bitwise_negation(val_false))