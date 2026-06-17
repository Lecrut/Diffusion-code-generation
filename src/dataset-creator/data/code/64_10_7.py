import datetime
def convert_date_formats(date_strings):
    results = []
    for d in date_strings:
        try:
            dt = datetime.datetime.strptime(d, "%d/%m/%Y")
            formatted = f"{dt.strftime('%B')} {dt.day}, {dt.year}"
            results.append(formatted)
        except ValueError:
            pass
    for d in date_strings:
        try:
            dt = datetime.datetime.strptime(d, "%Y-%m-%d")
            formatted = f"{dt.strftime('%B')} {dt.day}, {dt.year}"
            results.append(formatted)
        except ValueError:
            pass
    for d in date_strings:
        try:
            dt = datetime.datetime.strptime(d, "%B %d, %Y")
            formatted = f"{dt.strftime('%b')} {dt.day}, {dt.year}"
            results.append(formatted)
        except ValueError:
            pass
    return results
if __name__ == '__main__':
    sample_dates = [
        "15/03/2024",                                           
        "2024-08-10",                              
        "September 12, 2024"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ]
    valid_samples = [
        "15/03/2024",                                     
        "2024-08-10",                                      
    ]
    output = convert_date_formats(valid_samples)
    print(output[0])
    print(output[1])