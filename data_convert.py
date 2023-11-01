# should run in python3.6 with numpy==1.17
import numpy as np

from scipy.io import loadmat

def convert(mat_gt_pose_db_file,npy_gt_pose_db_file):
    gt_pose_db = loadmat(mat_gt_pose_db_file)
    actor_3d = np.array(
        np.array(gt_pose_db['actor3D'].tolist()).tolist()).squeeze()
    num_person = len(actor_3d)
    print(num_person)
    print(actor_3d)
    np.save(npy_gt_pose_db_file,actor_3d)

mat_gt_pose_db_file = 'data/Shelf/actorsGT.mat'
npy_gt_pose_db_file = 'data/Shelf/actorsGT.npy'
convert(mat_gt_pose_db_file, npy_gt_pose_db_file)

mat_gt_pose_db_file = 'data/Campus/actorsGT.mat'
npy_gt_pose_db_file = 'data/Campus/actorsGT.npy'
convert(mat_gt_pose_db_file, npy_gt_pose_db_file)