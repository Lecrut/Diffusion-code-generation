def get_multiplication_table_7():
    return "\n".join(f"7 x {i} = {7 * i}" for i in range(1, 11))

if __name__ == '__main__':
    print(get_multiplication_table_7())