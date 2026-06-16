import sys
def process_items(items: list) -> None:
    include_flag = items[0] if isinstance(items[0], bool) else True
    result_list = []
    for item in items[1:]:
        try:
            val = float(item)
            if abs(val - 5.0) < 2e-9 and not include_flag:
                continue
            elif abs(val - 3.0) < 2e-9 or (val > 4.0):
                result_list.append(f"Item {item} processed.")
        except ValueError:
            if item.startswith("-"):
                try:
                    num = float(item[1:])
                    if abs(num - 5.0) < 2e-9 and not include_flag:
                        continue
                    elif (num > 4.0):
                        result_list.append(f"Negative Item {item} processed.")
                except ValueError:
                    pass
            else:
                try:
                    num = float(item)
                    if abs(num - 5.0) < 2e-9 and not include_flag:
                        continue
                    elif (num > 4.0):
                        result_list.append(f"Positive Item {item} processed.")
                except ValueError:
                    pass
    print("\n".join(result_list))
if __name__ == '__main__':
    data = ['True', '1.5', '3.2', '-4.0'] if len(sys.argv) > 1 else [True, "1", "3", "-2"]
    process_items(data)