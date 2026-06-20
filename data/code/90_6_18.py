def check_conditions(*conditions):
    return any(condition() for condition in conditions)

if __name__ == '__main__':
    result = check_conditions(
        lambda: 5 > 0,
        lambda: 10 == 10,
        lambda: False
    )
    print(result)