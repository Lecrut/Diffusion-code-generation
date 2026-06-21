from datetime import datetime, timezone

DATE_FORMAT_MAP = {
    'iso': '%Y-%m-%dT%H:%M:%S%z',
    'standard': '%Y-%m-%d %H:%M:%S'
}

def sort_and_format_timestamps(timestamp_list, fmt_key='standard'):
    if not isinstance(timestamp_list, list):
        raise ValueError("Input must be a list")
    
    if not timestamp_list:
        return []
    
    for ts in timestamp_list:
        if not isinstance(ts, int):
            raise ValueError("All timestamps must be integers")
            
    if fmt_key not in DATE_FORMAT_MAP:
        raise ValueError("Unsupported format key")
        
    dt_objects = []
    for ts in timestamp_list:
        dt_obj = datetime.fromtimestamp(ts, tz=timezone.utc)
        dt_objects.append((dt_obj, dt_obj.strftime(DATE_FORMAT_MAP[fmt_key])))
        
    dt_objects.sort(key=lambda x: x[0])
    
    return [item[1] for item in dt_objects]

if __name__ == '__main__':
    sample_data = [1672531200, 1640995200, 1704067200, 1609459200]
    formatted_dates = sort_and_format_timestamps(sample_data)
    print(formatted_dates)