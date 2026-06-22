def multiplication_table_for_seven():
    result = []
    for i in range(1, 11):
        result.append(f"{i} x 7 = {i * 7}")
    return result

if __name__ == '__main__':
    print(multiplication_table_for_seven())