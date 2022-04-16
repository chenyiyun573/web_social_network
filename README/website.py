from pywebcopy import save_webpage

kwargs = {'project_name': 'site folder'}

save_webpage(

    # url pf the website
    url='https://cs198-75.org/web-hw/hw8/',

    # folder where the copy will be saved
    project_folder=r'C:\Users\chenyiyun\Desktop\project8\hw8\README',
    **kwargs
)
