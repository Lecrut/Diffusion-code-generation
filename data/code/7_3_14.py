def format_duration(time_string):
    parts = time_string.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    result_parts = []
    
    if days > 0:
        if days == 1:
            result_parts.append('1 Day')
        else:
            result_parts.append(f'{days} Days')
            
    if hours > 0:
        if hours == 1:
            result_parts.append('1 Hour')
        else:
            result_parts.append(f'{hours} Hours')
            
    if minutes > 0:
        if minutes == 1:
            result_parts.append('1 Minute')
        else:
            result_parts.append(f'{minutes} Minutes')
            
    if seconds > 0:
        if seconds == 1:
            result_parts.append('1 Second')
        else:
            result_parts.append(f'{seconds} Seconds')
            
    if len(result_parts) == 0:
        return '0 Seconds'
        
    if len(result_parts) == 1:
        return result_parts[0]
        
    last_part = result_parts[-1]
    first_parts = result_parts[:-1]
    
    return ', '.join(first_parts) + ', ' + last_part

if __name__ == '__main__':
    print(format_duration('00:00:00'))
    print(format_duration('01:00:00'))
    print(format_duration('25:30:45'))
    print(format_duration('48:00:00'))
    print(format_duration('73:05:10'))