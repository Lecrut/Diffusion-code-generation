def compute_exponentiation(base_value, power_value, modulo_value=None):
    result_base = base_value
    result_exp = power_value
    intermediate = pow(result_base, result_exp)
    if modulo_value is not None and modulo_value > 0:
        final_value = pow(result_base, result_exp, modulo_value)
    else:
        final_value = intermediate
    return final_value

if __name__ == '__main__':
    val_base = 5
    val_power = 3
    val_mod = 128
    computed_result = compute_exponentiation(val_base, val_power, val_mod)
    print(computed_result)