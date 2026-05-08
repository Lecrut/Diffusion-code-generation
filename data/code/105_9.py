from datetime import date
from dateutil.relativedelta import relativedelta
if __name__ == '__main__':
    start_date = date(2023, 10, 26)
    delta_months = 3
    next_date = start_date + relativedelta(months=delta_months)
    print(f"Start Date: {start_date}")
    print(f"Adding {delta_months} months")
    print(f"Next Date: {next_date}")