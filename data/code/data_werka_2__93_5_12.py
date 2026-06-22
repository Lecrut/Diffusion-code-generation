def both_false_check(a, b):
    is_first_false = a == False
    is_second_false = b == False
    combined_result = is_first_false and is_second_false
    yield combined_result

if __name__ == '__main__':
    val_a = True
    val_b = False
    generator_instance = both_false_check(val_a, val_b)
    output_values = list(generator_instance)
    print(output_values)