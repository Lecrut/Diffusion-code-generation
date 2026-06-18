import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file: str, output_file: str):
    """Read temperatures from a CSV file, convert them to Fahrenheit, and write to a new CSV file.

    Args:
        input_file: Path to the source CSV file containing temperature readings in Celsius.
                   Expected format: two columns 'index' (int) and 'temperature_celsius' (float).
        output_file: Path to the destination CSV file where converted Fahrenheit values will be written.
                     Output format: three columns 'original_index', 'celsius_value', 'fahrenheit_value'.

    Raises:
        FileNotFoundError: If the input file does not exist or cannot be read.
        ValueError: If a temperature value in the input is invalid (e.g., non-numeric).
        PermissionError: If there are insufficient permissions to write to the output file.
        IOError: For other generic I/O errors during reading or writing.

    Note:
        This function gracefully handles potential exceptions by raising informative error messages,
        preventing silent data loss while ensuring robust operation in automated environments.
    """
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Verify expected columns exist
            if not all(col in ['index', 'temperature_celsius'] for col in reader.fieldnames):
                raise ValueError(f"Unexpected column names in {input_file}: {reader.fieldnames}")

            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                # Write header row explicitly including original index for clarity
                writer.writerow(['original_index', 'celsius_value', 'fahrenheit_value'])

                count_processed = 0
                for idx, row in enumerate(reader):
                    try:
                        celsius_temp = float(row['temperature_celsius'])
                        fahrenheit_temp = round(celsius_to_fahrenheit(celsius_temp), 2)
                        
                        writer.writerow([int(idx + 1), str(row['index']), str(float(celsius_temp)), str(fahrenheit_temp)])
                        count_processed += 1
                        
                    except ValueError:
                        raise ValueError(
                            f"Invalid temperature value found at row {idx}: '{row.get('temperature_celsius', 'N/A')}' "
                            f"in file {input_file}. Please ensure all values are valid numbers."
                        )

        print(f"Successfully processed and converted {count_processed} records from '{input_file}' to '{output_file}'.")

    except FileNotFoundError:
        raise FileNotFoundError(f"The input CSV file was not found at path: {input_file}")
    except PermissionError as e:
        raise PermissionError(f"Insufficient permissions to write the output file. Path: {output_file}. Error details: {e}")
    except IOError as e:
        raise IOError(f"An I/O error occurred while processing files. Input: {input_file}, Output: {output_file}. Details: {str(e)}")

if __name__ == '__main__':
    # Hard-coded sample data for demonstration purposes (no user input or external dependencies)
    sample_input_data = [
        "index,temperature_celsius",
        "1,25.0",
        "2,-10.5",
        "3,100.0",
        "4,0.0"
    ]

    try:
        # Write sample data to a temporary in-memory style file handling via string write first? 
        # Since we cannot create files externally without pre-existing paths and must avoid network/inputs,
        # We will simulate the input by creating an embedded script that writes its own temp file or processes inline.
        
        # To strictly adhere to "no user input" and "runnable module", we can write a temporary CSV content string 
        # to disk within this same process if allowed, OR just generate output directly without reading external files?
        # The task says: "handle potential file I/O errors gracefully". It implies the logic must handle real files.
        # However, it also says sample block must run WITHOUT pre-existing files.
        
        # Strategy: Create a temporary input file path in memory (using a unique name), write content there programmatically 
        # before calling process_temperature_csv to simulate reading from a file, then delete the temp file if possible?
        # Or simpler: Just define the data and let the main block create the output by simulating the read logic inline 
        # but wrapped in the function structure for robustness demonstration.
        
        # Re-reading constraints: "The sample block must run without user input... or pre-existing files."
        # This means I cannot assume /data/temps.csv exists. I MUST generate it dynamically if reading, 
        # OR modify process_temperature_csv to accept data directly? No, signature is fixed by docstring logic usually.
        
        # Best approach for "Robust Script": Create a temporary file path using standard library (tempfile), write sample CSV there, run the function, then clean up.
        import tempfile
        
        temp_input_path = None
        try:
            # Generate unique filename safely in current process directory or temp dir? 
            # Use os.path.join for portability without external libs like pathlib if possible to keep it minimal robust script.
            # Actually `tempfile` is standard and safe.
            
            fd, temp_input_path = tempfile.mkstemp(suffix='.csv', prefix='sample_temp_')
            try:
                with os.fdopen(fd, 'w', encoding='utf-8') as f:
                    for line in sample_input_data[1:]: # Skip header manually written below or use csv writer? 
                        # Let's write raw lines to ensure exact match.
                        if len(line) > 0 and ',' not in line.split()[-2:].count(',') == False:
                            pass # Just appending
                
                # Actually, let's just construct the CSV content properly for tempfile fdopen above
                with open(temp_input_path + '.csv', 'w', newline='', encoding='utf-8') as f:
                    f.write(sample_input_data[1].replace('\n', '\r\n')) 
                
            finally:
                # Clean up temp file immediately after creation if needed, but we need it for the function call.
                pass
                
        except Exception as e:
            raise IOError(f"Failed to create temporary input sample file due to system restriction or error: {e}")

        output_path = 'converted_temperatures.csv'
        
        # Execute the core logic with our generated temp data
        process_temperature_csv(temp_input_path, output_path)
        
    finally:
        try:
            import os
            if os.path.exists(output_path):
                os.remove(output_path)
            print("Output file cleaned up.")
        except Exception as cleanup_err:
            # Log error but don't fail the script on this final step
            pass