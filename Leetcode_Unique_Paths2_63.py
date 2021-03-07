class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        
        arr = [[0 for i in range(cols)]  for j in range(rows)]
        obstacle = False; 
        
        for i in range(rows):
            if((obstacle==False) and (obstacleGrid[0][i] == 0)):
                arr[0][i]=1
                
            if (obstacleGrid[0][i] == 1):
                obstacle=True
                arr[0][i]=0
            
            if(obstacle==True):
                arr[0][i]=0
        
        col_obs=False
        for j in range(cols):
            if((col_obs==False) and (obstacleGrid[j][0] == 0)):
                arr[j][0]=1
                
            if(obstacleGrid[j][0] == 1):
                col_obs=True
                arr[j][0]=0

            if(col_obs==True):
                arr[j][0]=0
        
        
        for i in range(1,rows):
            for j in range(1,rows):
                if(obstacleGrid[i][j]!=1):
                    arr[i][j]= arr[i-1][j] + arr[i][j-1]
                
                else:
                    arr[i][j]=0
        
        return arr[rows-1][cols-1]
            
            
