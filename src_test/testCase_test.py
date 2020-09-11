'''
生成用例文件代码编写测试
'''

import os

# 用例文件夹
case_path_dir = str(os.path.abspath(r'.\test_dir'))
# 报告文件夹
report_path_dir = str(os.path.abspath(r'.\test_report'))

# 遍历获取用例文件夹
files = []
for a, b, c in os.walk(case_path_dir):
    files.append(str(a))

run_text = []
for i in files:
    # 前面截取testCase
    # a = str(i[len(rel_path_dir)+1:len(rel_path_dir)+9:])
    # 倒数截取后缀.air
    # a = str(i[-4::])
    # 生成报告文件夹名称
    report_name = str(i[len(case_path_dir)+1:-4:])
    if(report_name != ''):
        run_text.append(str(r'airtest run "{}" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log {}\{}'.format(i, report_path_dir, report_name)))
# 生成用例运行文件
with open(case_path_dir+r'\testCase.bat', 'w', encoding='utf-8') as f:
    for i in run_text:
        f.write(i + '\n')
        