def int_to_english(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('Input must be a non-negative integer')
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + '-' + ones[ones_digit]
if __name__ == '__main__':
    print(int_to_english(5))
    print(int_to_english(12))
    print(int_to_english(42))
    print(int_to_english(99))