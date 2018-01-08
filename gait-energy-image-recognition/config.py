
import os
class project:

    project_path = '/home/me/Desktop/python'
    casia_dataset_b_path = "%s/gei" % project_path
    
    casia_test_img = "%s/001/bg-01/001-bg-01-090.png" % casia_dataset_b_path
    #casia_test_img = "%s/001/bg-01/090/001-bg-01-090-038.png" % casia_dataset_b_path

    casia_test_img_dir = "%s/004/nm-01" % casia_dataset_b_path

    test_data_path = "%s/data/test/" % project_path

    if not os.path.exists(test_data_path):
        os.makedirs(test_data_path)
