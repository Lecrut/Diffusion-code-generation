def compare_two_simple_quantities_now_run_examples(quantity1, quantity2):
    if quantity1 > quantity2:
        return "The first quantity is greater than the second quantity."
    elif quantity1 < quantity2:
        return "The first quantity is less than the second quantity."
    else:
        return "The two quantities are equal."

if __name__ == '__main__':
    sample_quantity1 = 45
    sample_quantity2 = 30
    result = compare_two_simple_quantities_now_run_examples(sample_quantity1, sample_quantity2)
    print(result)