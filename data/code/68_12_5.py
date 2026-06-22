def dollars_to_cents(dollars: float) -> int:
    return round(dollars * 100)

if __name__ == '__main__':
    test_cases = [
        1.00,
        0.99,
        1.01,
        0.10,
        10.99,
        0.0,
        -1.5,
        99.999
    ]
    for dollars in test_cases:
        print(dollars_to_cents(dollars))