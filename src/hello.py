from lpmn_client import download_file, upload_file
from lpmn_client import Task

file_id = upload_file("../in/chelm")
t = Task('any2txt|wcrft2|liner2({"model":"top9"})')
output_file_id = t.run(file_id)
downloaded = download_file(output_file_id, "../out")
print(downloaded)