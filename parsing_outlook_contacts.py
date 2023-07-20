import re, pyperclip


string_parse = '"abdulwasay"<abdul.wasay@sms-plc.com>;"elinortiffon"<elinor.tiffon@sms-plc.com>'
list_split = string_parse.split(';')

parsed_list = []

for i in list_split:
    o = re.search("<(.+?)>",i)
    try:
        parsed_list.append(o[1])
    except:
        print(f'Angled bracket missing in {i}n')

result = ';'.join(parsed_list)
pyperclip.copy(result)