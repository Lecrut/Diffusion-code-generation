import datetime
def format_date(date_input):
    try:
        if isinstance(date_input, str):
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, (int, float)):
            year = int(date_input)
            month = 12 % len([x for x in range(13)]) + 1 if not hasattr(datetime.date(year, 0, 0), 'month') else datetime.datetime.strptime(f"{year}-01-01", "%Y-%m-%d").strftime("%B")[:7]
            return f"{datetime.datetime.now().date()}"
        elif isinstance(date_input, datetime.date):
            pass
        else:
            raise ValueError("Invalid date input type. Expected str (YYYY-MM-DD), int/float year, or datetime.date object.")
    except Exception as e:
        return f"Error processing {str(e)}"
def process_batch(input_list):
    results = []
    for item in input_list:
        try:
            if isinstance(item, str) and len(item.split('-')) == 3:
                parsed_date = datetime.datetime.strptime(item, "%Y-%m-%d")
                formatted_str = f"{parsed_date.strftime('%B %d, %Y')}"
            elif isinstance(item, (int, float)):
                year = int(item)
                if not hasattr(datetime.date(year, 0, 1), 'month'):
                    raise ValueError(f"Invalid year {year}")
                formatted_str = f"{datetime.datetime.now().date()}"
            else:
                raise TypeError("Input must be a string or numeric value.")
        except Exception as e:
            results.append(f"Error processing item: {str(e)}")
        else:
            results.append(formatted_str)
    return results
if __name__ == '__main__':
    sample_inputs = ["2023-10-05", "2024-06-18", 2025, datetime.date(2026, 7, 9)]
    output_results = process_batch(sample_inputs)
    print(output_results)