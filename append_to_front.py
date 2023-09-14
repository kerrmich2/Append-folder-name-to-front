import os

# Read ALL files (even in subdirectories) into a single list, including path names.
def all_files(directory):
    file_list = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_list.append(os.path.join(dirpath, file).replace("\\", "/"))

    return file_list

# Append year to the front of a file.
def dneppa(file, year):
    count = 0

    # Find where the first "/" is from the end.
    for i in file[::-1]:
        if i == "/":
            break
        count += 1

    # Add the year to the front of the filename, after the first "/".
    new_file = (file[::-1][:count] + "-" + str(year)[::-1] + file[::-1][count:])[::-1]

    return new_file

d = root_dir

file_list = all_files(d)

# Append i to the start of the file name.
for i in range(2020, 2023):
    d += "/" + str(i)
    for file in all_files(d):
        os.rename(file, dneppa(file, i))
    d = root_dir


























































