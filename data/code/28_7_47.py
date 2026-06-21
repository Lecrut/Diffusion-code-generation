def is_larger(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be either int or float.')
        return a > b
    except Exception as e:
        print(f'Error: {e}')
        return False
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(3, 7))
    print(is_larger(-1, -2))
    print(is_larger(0, 0))
    print(is_larger('a', 5))