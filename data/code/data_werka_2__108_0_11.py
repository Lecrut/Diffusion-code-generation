import datetime

DAY_OF_MONTH_MAP = {
    "day": lambda d: d.day,
    "month": lambda d: d.month,
    "year": lambda d: d.year,
}

def extract_date_component(date_obj, component_name):
    if component_name not in DAY_OF_MONTH_MAP:
        raise ValueError(f"Unsupported component: {component_name}")
    return DAY_OF_MONTH_MAP[component_name](date_obj)

if __name__ == '__main__':
    sample_date = datetime.date(2024, 12, 25)
    component = "day"
    result = extract_date_component(sample_date, component)
    print(result)