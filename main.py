def remove_empty_lines(filename):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove empty lines
    non_empty_lines = [line for line in lines if line.strip()]

    # Write the non-empty lines back to the file
    with open(filename, 'w') as file:
        file.writelines(non_empty_lines)

# Provide the path to the text file
file_path = 'C:/xxx/Documents/Projekte/SchulenNRW/CSV/BR/Text.txt'

# Call the function to remove empty lines
remove_empty_lines(file_path)
