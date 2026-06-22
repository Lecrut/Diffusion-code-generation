import datetime

def convert_date(date_obj):
    FORMATS = {
        "INPUT": "%Y-%m-%d",
        "OUTPUT": "%A, %B %d, %Y"
    }
    try:
        formatted_date = date_obj.strftime(FORMATS["OUTPUT"])
        return formatted_date
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    sample_date = datetime.datetime(2021, 1, 1)
    result = convert_date(sample_date)
    print(result)