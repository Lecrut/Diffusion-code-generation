def ml_to_lit(ml):
    try:
        return ml / 1000
    except OverflowError:
        print('Overflow error occurred.')
        return None
if __name__ == '__main__':
    result = ml_to_lit(2500)
    print(result)