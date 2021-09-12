import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import random
import heapq



def dijkstra_np(info_list, start_node, node_cnt=None):
    # info_list에는 start_node, end_node, distance가 들어있음
    node_dist_info = defaultdict(list)#{}
    for s_vertex, e_vertex, dist in info_list:
        node_dist_info[s_vertex].append([e_vertex, dist])
        node_dist_info[e_vertex].append([s_vertex, dist])
    # 01. 모든 노드의 거리를 inf값으로 설정한다
    # 노드번호, 떨어진 거리, 방문여부
    columns = ['num', 'dist', 'visit']
    cdict = dict(zip(columns, range(len(columns))))
    arr = np.zeros((node_cnt, len(columns)), dtype=np.int32)
    arr[:,cdict['num']] = np.arange(1, node_cnt+1) # 노드번호가 1번부터라면
    arr[:,cdict['dist']] = 2 ** 31 - 1 #np.inf
    arr[start_node-1, cdict['dist']] = 0
    while arr[:,cdict['visit']].sum()!=node_cnt: # 방문하면 1로 바뀜
        no_visit = arr[np.where(arr[:,cdict['visit']]==0)] # 방문안한 ind            
        cur_node = no_visit[no_visit[:, cdict['dist']]==no_visit[:, cdict['dist']].min(), cdict['num']][0]
        arr[cur_node-1, cdict['visit']] = 1 # 방문으로 변경
        for end_node, dist in node_dist_info[cur_node]:
            if arr[end_node-1, cdict['visit']] == 0: # 방문안한 곳이면
                # 새로 거리 계산하고 
                if arr[cur_node-1, cdict['dist']]+dist < arr[end_node-1, cdict['dist']]:# 더 작으면 변경
                    arr[end_node-1, cdict['dist']] = arr[cur_node-1, cdict['dist']]+dist 
    return arr







