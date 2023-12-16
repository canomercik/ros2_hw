from setuptools import setup

package_name = 'can_omercik'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='can',
    maintainer_email='ahmetcan7754@gmail.com',
    description='Hello World Test',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'talker = can_omercik.publisher_member_function:main',
        	'listener = can_omercik.subscriber_member_function:main',
        ],
    },
)
