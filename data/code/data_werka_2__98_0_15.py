def evaluate_state(status_code, temperature, pressure):
    state_map = {
        200: "normal",
        400: "warning",
        500: "critical"
    }
    
    if status_code not in state_map:
        raise ValueError("Unsupported status code")
    
    base_state = state_map[status_code]
    
    if base_state == "normal":
        if temperature < 30 and pressure < 100:
            return "stable"
        elif temperature >= 30 and temperature < 40:
            return "warming"
        else:
            return "overheating"
    elif base_state == "warning":
        if temperature < 20:
            return "cooling_warning"
        elif pressure > 120:
            return "pressure_warning"
        else:
            return "general_warning"
    elif base_state == "critical":
        if temperature > 50:
            return "critical_heat"
        elif pressure > 150:
            return "critical_pressure"
        else:
            return "system_failure"
    return "unknown"

if __name__ == '__main__':
    code = 200
    temp = 35
    press = 90
    result = evaluate_state(code, temp, press)
    print(result)
    
    code = 400
    temp = 15
    press = 110
    result = evaluate_state(code, temp, press)
    print(result)
    
    code = 500
    temp = 55
    press = 140
    result = evaluate_state(code, temp, press)
    print(result)