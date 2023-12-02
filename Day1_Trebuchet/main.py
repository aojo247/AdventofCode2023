input_file = 'input.txt'

with open(input_file, 'r') as file:
    content = file.readlines()



def get_ints_from_string(string, loc1=0, loc2=-1):
    int_list = []
    for i in string:
        if i.isdigit():
            int_list.append(int(i))

    if len(int_list) >= 2:
        return_list = [int_list[loc1], int_list[loc2]]
    elif len(int_list) == 1:
        return_list = [int_list[loc1], int_list[loc1]]
    else:
        return_list = []

    return return_list


total_list = []
for x in content:
    row_data = get_ints_from_string(x)
    combined_nums = int(''.join(map(str, row_data)))
    print(combined_nums)
    total_list.append(combined_nums)


print(sum(total_list))