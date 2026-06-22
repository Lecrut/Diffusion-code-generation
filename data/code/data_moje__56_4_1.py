def multiplication_table_5():
    return [f"5 x {i} = {5 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    print('\n'.join(multiplication_table_5()))