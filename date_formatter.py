import csv

input_csv_file = 'data/earthquake_data.csv'
# Replace 'output.csv' with the desired name of your new CSV file
output_csv_file = 'output.csv'  

datetime_list = []

# Open the CSV file in read mode
with open(input_csv_file, 'r', newline='', encoding="utf-8") as csv_infile, open(output_csv_file, 'w', newline='') as csv_outfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_infile)
    csv_writer = csv.writer(csv_outfile)

    # Iterate over the rows in the CSV file
    headers = csv_reader.__next__()
    csv_writer.writerow(headers)
    for row in csv_reader:
        # Each row is a list of values
        datetime_str = row[2]
        old_datetime_str = datetime_str
        parts = datetime_str.split(" ")
        # Split the date using hyphen as a separator
        date_parts = parts[0].split("-")
        # Swap the first two numbers in the date_parts list
        date_parts[0], date_parts[1] = date_parts[1], date_parts[0]
        # Join the modified date parts and the time part back together
        modified_date_and_time = "-".join(date_parts) + " " + parts[1]
        row[2] = modified_date_and_time
        csv_writer.writerow(row)











    

    

