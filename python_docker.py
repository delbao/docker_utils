# doc: http://containertutorials.com/py/docker-py.html

import docker

docker_client = docker.Client(base_url='unix://var/run/docker.sock',
                              version='auto')

dockerfile_path = os.path.dirname(os.path.abspath(__file__))

docker_image_name = 'cc_test_print'
dt_now = datetime.datetime.now()
docker_container_name = docker_image_name + dt_now.strftime('_cont_%m.%d.%Y_')

container = docker_client.create_container(image=docker_image_name, 
                                           name = (docker_container_name))

# id = container['Id']
# docker_client.start(id)
docker_client.start(container)

# remove docker container
docker_client.remove_container(id, force=True)
# don't remove only stop the container
docker_client.stop(id)
