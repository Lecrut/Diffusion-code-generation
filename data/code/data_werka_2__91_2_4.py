def negate_boolean(is_active):
    return not is_active

if __name__ == '__main__':
    is_active = True
    result = negate_boolean(is_active)
    print(result)