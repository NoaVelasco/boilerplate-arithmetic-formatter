def arithmetic_arranger(problems, *boolean):
    op_list = []
    errors = []
    err_prompt = {
        'prob': "Error: Too many problems.",
        'dig': "Error: Numbers must only contain digits.",
        'num': "Error: Numbers cannot be more than four digits.",
        'oper': "Error: Operator must be '+' or '-'."
    }
    if len(problems) > 5:
        errors.append("prob")

    else:
        for op in problems:
            elem = op.split()
            x = elem[0].isdigit()
            z = elem[2].isdigit()

            if x is False or z is False:
                errors.append("dig")
                break

            if (len(elem[0]) > 4 or len(elem[2])) > 4:
                errors.append("num")
                break

            if elem[1] != '+' and elem[1] != '-':
                errors.append("oper")
                break

            if bool(errors) is False:
                op_list.append(elem)

    for err in errors:
        return err_prompt[err]

    if bool(errors) is False:
        long_tot = []
        max_i = []
        spc_fix = '    '

        for i in op_list:
            long_i = []
            for sub in i:
                long_i.append(len(sub))
            long_i.append(max(long_i)+2)
            long_tot.append(long_i)
            max_i.append(max(long_i))

        line_output_1 = []
        line_output_2 = []
        line_output_3 = []
        line_output_4 = []
        
        # Try enumerate in the future
        for x in range(len(op_list)):
            if long_tot[x][0] > long_tot[x][2]:
                line_output_1.append(f'  {op_list[x][0]}')
                temp_spc = long_tot[x][3] - long_tot[x][2] - 1
                line_output_2.append(op_list[x][1] + temp_spc * ' ' + op_list[x][2])
                line_output_3.append(long_tot[x][3] * '-')

            else:
                temp_spc = long_tot[x][3] - long_tot[x][0]
                line_output_1.append(temp_spc * ' ' + op_list[x][0])
                line_output_2.append(op_list[x][1] + ' ' + op_list[x][2])
                line_output_3.append(long_tot[x][3] * '-')

            line_output_1.append(spc_fix)
            line_output_2.append(spc_fix)
            line_output_3.append(spc_fix)
            
            if True in boolean:
                if op_list[x][1] == "-":
                    operation = str(int(op_list[x][0]) - int(op_list[x][2]))
                if op_list[x][1] == "+":
                    operation = str(int(op_list[x][0]) + int(op_list[x][2]))
                temp_spc = long_tot[x][3] - len(operation)
                line_output_4.append(temp_spc * ' ' + operation)
                line_output_4.append(spc_fix)

        line_output_1[-1] = '\n'
        line_output_2[-1] = '\n'
        
        if True in boolean:
            line_output_3[-1] = '\n'
            line_output_4.pop()
            output = ''.join(line_output_1 + line_output_2 + line_output_3 + line_output_4)
            
        else:
            line_output_3.pop()
            output = ''.join(line_output_1 + line_output_2 + line_output_3)
        
        return output
