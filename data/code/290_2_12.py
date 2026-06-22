def tons_to_kg(tons):
    return int(tons * 907.184)

if __name__ == '__main__':
    tons_value = 25
    kg_value = tons_to_kg(tons_value)
    print(f"{tons_value} tons is {kg_value} kg")