def dollars_to_cents(dollars_str):
    parts = dollars_str.split('.')
    whole_dollars = int(parts[0])
    cents_part = 0
    if len(parts) > 1:
        fractional = parts[1]
        if len(fractional) == 0:
            cents_part = 0
        elif len(fractional) == 1:
            cents_part = int(fractional) * 10
        else:
            cents_part = int(fractional[:2])
            if len(fractional) > 2 and int(fractional[2:]) > 49:
                cents_part += 1
            if len(fractional) > 2 and int(fractional[2:]) == 50:
                if cents_part % 2 != 0:
                    cents_part += 1
    negative = whole_dollars < 0
    if negative:
        total_cents = -(abs(whole_dollars) * 100 + cents_part)
    else:
        total_cents = whole_dollars * 100 + cents_part
    return total_cents

if __name__ == '__main__':
    sample_values = [
        "10.00",
        "0.99",
        "123.456",
        "-42.50",
        "5.01",
        "0.005",
        "999.999",
        "-0.01",
        "0.00",
        "1.005"
    ]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)